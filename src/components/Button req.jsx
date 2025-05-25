import React from "react";

const Button = ({ styles }) => (
  <button
    type="button"
    onClick={() => window.location.href = "./Others/Proposal.html"}
    className={`py-4 px-6 font-poppins font-medium text-[18px] text-primary bg-blue-gradient rounded-[10px] outline-none ${styles}`}
  >
    Read Proposal
  </button>
);

export default Button;
