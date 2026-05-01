
function addEmployee(){
    var EmpId = document.getElementById("EmpId").value
    var Name = document.getElementById("Name").value
    var Des = document.getElementById("Des").value
    var table = document.getElementById("table1");
    var row = table.insertRow();
    row.insertCell(0).innerText = EmpId
    row.insertCell(1).innerText = Name
    row.insertCell(2).innerText = Des

    document.getElementById("EmpId").value = ""
    document.getElementById("Name").value = ""
    document.getElementById("Des").value =""
}
