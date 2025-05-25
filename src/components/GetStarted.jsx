import styles from "../style";
import { arrowUp } from "../assets";

const GetStarted = () => (
  <section id="" className={`${styles.paddingY} ${styles.flexCenter} flex-col relative `}>
  <a href="./Others/Litrature.html">
  <div className={`${styles.flexCenter} w-[140px] h-[140px] rounded-full bg-blue-gradient p-[2px] cursor-pointer`}>
    <div className={`${styles.flexCenter} flex-col bg-primary w-[100%] h-[100%] rounded-full`}>
      <div className={`${styles.flexStart} flex-row`}>
        <p className="font-poppins font-medium text-[18px] leading-[23.4px]">
          <span className="text-gradient">Litrature</span>
        </p>
        <img src={arrowUp} alt="arrow-up" className="w-[23px] h-[23px] object-contain" />
      </div>
      
      <p className="font-poppins font-medium text-[18px] leading-[28px]">
        <span className="text-gradient">Review</span>
      </p>
    </div>
  </div>
  </a>
  </section>

);

export default GetStarted;