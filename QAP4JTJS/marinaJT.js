//Author: Joey Thomas
//Date: Nov. 17, 2024
//Description: A program for the St. Johns Marina & Yacht Club to create receipts.

//Constants.
const cur2format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
});

const MARINA_SITES = 100; //Total # of sites.
const EVEN_SITE_RATE = 80.00; //Per month.
const ODD_SITE_RATE = 120.00; //Per month.
const ALT_MEM_RATE = 5.00; //Per person per month.
 
const WEEK_CLEAN_RATE = 50.00; //Per month.
const VID_SURV_RATE = 35.00; //Per month.
 
const HST_RATE = 0.15; //15%.
const STAN_MEM_DUES = 75.00; //Per month.
const EXEC_MEM_DUES = 150.00; //Per month.
 
const PROC_FEE = 59.99; 
const CANCEL_FEE = 0.60; //60%.

//Main program.
//Input.
let curDat = prompt("Enter The Current Date (YYYY-MM-DD): ");
let sitNum = parseInt(prompt("Enter Member's Site Number (1-100): "));

let memNam = prompt("Enter Member's Name: ");
let strAdd = prompt("Enter Member Street Address: ");
let City = prompt("Enter Member's Residing City: ");
let Prov = prompt("Enter Member's Residing Province: ");
let posCod = prompt("Enter Member's Postal Code: ");

let phoNum = prompt("Enter Member's Phone Number (##########): ");
let celNum = prompt("Enter Member's Cell Number (##########): ");

let memTyp = prompt("Executive or Standard Membership Type? (S/E):").toUpperCase();
let altMem = parseInt(prompt("Enter Number of Alternative Members: "));

let weeCle = prompt("Would you like weekly site cleaning? (Y/N): ").toUpperCase();
let vidSur = prompt("Would you like video surveillance? (Y/N): ").toUpperCase();

//Processing.
if(sitNum % 2 == 0) { 
    sitCos = EVEN_SITE_RATE; 
} else{ 
    sitCos = ODD_SITE_RATE; 
} 
memCos = altMem * ALT_MEM_RATE; 
sitCha = memCos + sitCos; 
 
let extCos = 0 
if(weeCle == "Y") { 
    var weeLit = "Yes"; 
    extCos += WEEK_CLEAN_RATE; 
} else{ 
    var weeLit = "No"; 
} 

if(vidSur == "Y") { 
    var vidLit = "Yes"; 
    extCos += VID_SURV_RATE; 
} else{ 
    var vidLit = "No"; 
} 
 
let subTot = extCos + sitCha; 
let subTax = subTot * HST_RATE; 
let monTotal = subTot + subTax; 
 
let memDue = 0; 
if(memTyp == "E") { 
    var memTypLit = "Executive"; 
    memDue = EXEC_MEM_DUES; 
} else{ 
    var memTypLit = "Standard"; 
    memDue = STAN_MEM_DUES; 
} 
let totMonFee = monTotal + memDue; 
 
let totYeaFee = totMonFee * 12; 
let monPay = (totYeaFee + PROC_FEE) / 12; 
 
let canFee = (sitCha * 12) * CANCEL_FEE; 
  
//Output.
document.write("<table class='receipttable'>");

document.write("<tr class='centertext'>");
document.write("<th colspan='2'>St. John's Marina & Yacht Club<br>Yearly Member Receipt</th>");
document.write("</tr>");

document.write("<tr>");
document.write("<td colspan='2'><br>Client Name and Address:<br>&nbsp;</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td colspan='2'>" + memNam + "<br>" + strAdd + "<br>" + City + ", " + Prov + " " + posCod + "<br><br>");
document.write("Phone: " +  phoNum + " (H)<br>" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + celNum + " (C)" + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Site #: " + sitNum + "</td><td class='righttext' id='noleft'>" + "Membership Type: " + memTypLit + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Alternate Members:<br>Weekly site cleaning:<br>" + "Video surveillance:</td>")
document.write("<td class='righttext' id='noleft'>" + altMem + "<br>" + weeLit + "<br>" + vidLit + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Site charges:<br>Extra charges:</td>")
document.write("<td class='righttext' id='noleft'>" + cur2format.format(sitCha) + "<br>" + cur2format.format(extCos) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Subtotal:<br>Sales tax (HST):</td>");
document.write("<td class='righttext' id='noleft'>" + cur2format.format(subTot) + "<br>" + cur2format.format(subTax) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Total monthly charges:<br>Monthly dues:</td>");
document.write("<td class='righttext' id='noleft'>" + cur2format.format(monTotal) + "<br>" + cur2format.format(memDue) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Total monthly fees:<br>Total yearly fees:</td>");
document.write("<td class='righttext' id='noleft'>" + cur2format.format(totMonFee) + "<br>" + cur2format.format(totYeaFee) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Monthly payment:</td>");
document.write("<td class='righttext' id='noleft'>" + cur2format.format(monPay) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td id='noright'>Issued:<br><br>HST Reg No:<br><br>Cancellation Fee:</td>");
document.write("<td class='righttext' id='noleft'>" + curDat + "<br><br>" + "549-33-5849-47<br><br>" + cur2format.format(canFee) + "</td>");
document.write("</tr>");

document.write("</table>");