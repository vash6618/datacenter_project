import React, { useState, useEffect } from 'react';

const ClientStatus = ({clientId}) => {
  const [message, setMessage] = useState("Success")
  const [local_client_id, setLocalClientId] = useState(0);
  const [loan_id, setLoanId] = useState(0);
  const [client_name, setClientName] = useState(0);
  const [loan_amount, setLoanAmount] = useState(0);
  const [loan_amount_remaining, setLoanAmountRemaining] = useState(0);
  const [loan_term, setLoanTerm] = useState(0);
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    if(clientId) {
      fetch('http://localhost:5000/clientstatus', {
        method: "POST",
        headers: { 'Content-Type': "application/json"},
        body: JSON.stringify({clientId})
      }
      ).then(res => res.json()).then(data => {
        console.log(data)
        setMessage(data.message)
        var client = data.client_data.client
        var loan_details = data.client_data.loan_details
        setLocalClientId(client.bank_id)
        setClientName(client.name)

        if(loan_details === null) {
          return;
        } 
        setLoanId(client.loan_id)
        setLoanTerm(loan_details.loan_term_months)
        setLoanAmount(loan_details.loan_amount)
        setLoanAmountRemaining(loan_details.loan_amount_remaining)

        var transactions_pl = data.client_data.transactions 
        if(data.message!=="Success" || transactions_pl===null) {
          return;
        }

        var transactions_li = ""        
        var key, val
        for([key, val] of Object.entries(transactions_pl)) {
          transactions_li += `<li key=${key}>${val.transaction_id}: ${val.amount_paid}</li>`
        }
        setTransactions(transactions_li)

      });
    }
  }, [clientId]);

  return (
    <div className="pad">
      <h1>Client Status of {clientId}</h1>
      <div>Client ID: {local_client_id} <br/>Client Name: {client_name} <br/>Loan ID: {loan_id}<br/></div>
      <div>Loan Amount: {loan_amount} <br/>Loan Term: {loan_term} <br/>Loan Amount Remaining: {loan_amount_remaining}<br/></div>
      <br/>
      { message === "Success" &&
        <div>Loan Approved. Please pay it back xD</div>
      }
      { message === "Success" &&
        <ul dangerouslySetInnerHTML={{__html: transactions}}></ul>
      }
      { message !== "Success" &&
        <div>{message}</div>
      }
    </div>
  );
}

export default ClientStatus;