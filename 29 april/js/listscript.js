function addCountry(){
    var country=document.getElementById("txtCountry").value;
    console.log("within addCountry "+country)    
    var listItem=document.createElement("li")
    listItem.innerText=country;
    var orderedList=document.getElementById("listOfCountries")
    orderedList.appendChild(listItem)
    document.getElementById("txtCountry").value=""

}