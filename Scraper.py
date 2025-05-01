import nest_asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import csv

# Apply nest_asyncio so the event loop works in Jupyter
nest_asyncio.apply()

# Function to scrape parking data for the specific city
async def scrape_parking_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Target city URL
        city_url = '/P27-osaka/C127/'
        city_name = 'Kita-ward'  # Replace with actual city name
        
        print(f"\nScraping parking data for city: {city_name}")

        # Navigate to the selected city page
        await page.goto(f'https://times-info.net{city_url}')
        await page.wait_for_selector('ul.p-parkingList_area > li', timeout=10000)

        # Get all parking lot entries
        parking_blocks = await page.query_selector_all('ul.p-parkingList_area > li')
        print(f"Found {len(parking_blocks)} parking lots in {city_name}.")

        # Create a CSV file to save the results
        with open(f'osaka_parking_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['Timestamp', 'Region', 'City', 'Name', 'Status', 'Count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write headers only if the file is empty
            csvfile.seek(0, 2)  # Move the pointer to the end of the file
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write parking data for each parking lot
            for block in parking_blocks:
                name_el = await block.query_selector('.s_ichiran_info_name')
                status_el = await block.query_selector('.p-parkingList_colmun_detail_status_manku')
                count_el = await block.query_selector('.s_ichiran_info_count')
               # distance_el = await block.query_selector('.s_ichiran_info_dist')

                name = await name_el.inner_text() if name_el else ''
                status = await status_el.inner_text() if status_el else ''
                count = await count_el.inner_text() if count_el else ''
              #  distance = await distance_el.inner_text() if distance_el else ''

                writer.writerow({
                    "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "Region": "大阪",
                    "City": city_name,
                    "Name": name.strip(),
                    "Status": status.strip(),
                    "Count": count.strip(),
                  #  "Distance": distance.strip()
                })

        print(f"Parking data for {city_name} has been saved to CSV.")

        await browser.close()

# Start the scraping process
await scrape_parking_data()
