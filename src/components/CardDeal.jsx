import { card } from "../assets";
import styles, { layout } from "../style";
import Button from "./Button report";

const CardDeal = () => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Find more about <br className="sm:block hidden" /> Our weekly Progress reports.
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
      Stay updated on our developments, milestones, and the latest improvements 
      as we work towards delivering the best smart parking solution.
      </p>

      <Button styles={`mt-10`} />
    </div>

    <div className={layout.sectionImg}>
      <img src={card} alt="billing" className="w-[100%] h-[100%]" />
    </div>
  </section>
);

export default CardDeal;
