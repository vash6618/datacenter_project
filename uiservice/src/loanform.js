import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./css/loanform.css"

const LoanForm = ({clientId}) =>  {
  const [gender, setGender] = useState(0);
  const [married, setMarried] = useState(1)
  const [selfEmployed, setSelfEmployed] = useState(1)
  const [creditHistory, setCreditHistory] = useState(1)
  const [education, setEducation] = useState(1)
  const [propertyArea, setPropertyArea] = useState(0)
  const [income, setIncome] = useState('')
  const [loanAmount, setLoanAmount] = useState('')
  const [loanTerm, setLoanTerm] = useState('')
  const [loanState, setLoanState] = useState(true)
  const navigate = useNavigate()

  const handleSubmit = (e) => {
    e.preventDefault();
    const loan_details = {gender, married, selfEmployed, creditHistory, education, propertyArea, income, loanAmount, loanTerm, clientId}
    fetch("http://localhost:5000/loanform", {
      method: "POST",
      headers: { 'Content-Type': "application/json"},
      body: JSON.stringify(loan_details)
    }).then(res => res.json()).then((data) => {
      console.log(data, typeof data.message);
      if (data.message === "Loan rejected") {
        setLoanState(false);
      } else {
        navigate('/clientstatus');
      }
    })
  }

  return (
    <div className="pad">
      <h1>Loan Applicant Details </h1>
      <br/>
      <form onSubmit={handleSubmit}>
        <div className="input-group mb-3">
          Gender:  
          <select className="internalpadding" id="inputGroupSelect00" name="gender" value={gender} onChange={(e) => setGender(e.target.value)}>
            <option value="0">Male</option>
            <option value="1">Female</option>
          </select>
        </div>
        <div className="input-group mb-3">
          Married:  
          <select className="custom-select internalpadding" id="inputGroupSelect01" name="married" value={married} onChange={(e) => setMarried(e.target.value)}>
            <option value="1">Yes</option>
            <option value="0">No</option>
          </select>
        </div>
        <div className="input-group mb-3">
          Self Employed:  
          <select className="custom-select internalpadding" id="inputGroupSelect02" name="self_employed" value={selfEmployed} onChange={(e) => setSelfEmployed(e.target.value)}>
            <option value="1">Yes</option>
            <option value="0">No</option>
          </select>
        </div>
        <div className="input-group mb-3">
          Credit History:  
          <select className="custom-select internalpadding" id="inputGroupSelect03" name="credit_history" value={creditHistory} onChange={(e) => setCreditHistory(e.target.value)}>
            <option value="1">Yes</option>
            <option value="0">No</option>
          </select>
        </div>
        <div className="input-group mb-3">
          Education:
          <select className="custom-select internalpadding" id="inputGroupSelect04" name="education" value={education} onChange={(e) => setEducation(e.target.value)}>
            <option value="0">Not graduate</option>
            <option value="1">Graduate</option>
          </select>
        </div>
        <div className="input-group mb-3">
          Property Area
          <select className="custom-select internalpadding" id="inputGroupSelect05" name="prop_area" value={propertyArea} onChange={(e) => setPropertyArea(e.target.value)}>
            <option value="2">Urban</option>
            <option value="0">Rural</option>
          </select>
        </div>

        Applicant Income(in $ per month): <input type="number" id="inputGroupSelect06" name="applicant_income" required value={income} onChange={(e) => setIncome(e.target.value)}></input><br/><br/>

        LoanAmount(in $): <input type="number" id="inputGroupSelect07" name="loan_amount" required value={loanAmount} onChange={(e) => setLoanAmount(e.target.value)}></input><br/><br/>

        Loan Amount Term(number of months): <input type="number" id="inputGroupSelect08" name="loan_term" required value={loanTerm} onChange={(e) => setLoanTerm(e.target.value)}></input><br/><br/>

        <button type="submit" className="btn btn-primary" value="GetLoanPrediction">Get Loan Prediction</button>
      </form>
      { !loanState && <div>Loan is rejected!</div>}
    </div>
  );

}

export default LoanForm;