const iValue = document.getElementById("todoinput");
console.log(iValue, "input tag");

const addBtn = document.getElementById("addBtn");
const errMsg = document.getElementById("erroMsg");
function showError(erMsg) {
  errMsg.textContent = erMsg;
  setTimeout(() => {
    errMsg.textContent = "";
  }, 2000);
}
addBtn.addEventListener("click", () => {
  const iValueData = iValue.value.trim(); //#""
  console.log(iValueData, "input data");
  if (!iValueData) {
    showError("pls enter any task to add");
  }
  const todosList = JSON.parse(localStorage.getItem("totalTodos")) || [];
  let new_task = {
    task: iValueData,
  };
  todosList.push(new_task); // [{},{}]
  localStorage.setItem("totalTodos", JSON.stringify(todosList));
  iValue.value=""
});
function displayTodos(){
    let allTodoosTagContainer=document.getElementById("containerTodos")
 allTodoosFromLs= JSON.parse(localStorage.getItem("totalTodos"))
 allTodoosFromLs.forEach((todo,index)=>{
    const liTag=document.createElement("li")
    liTag.innerHTML=`
    ${todo.task}
    `
    allTodoosTagContainer.append(liTag)
 })
}
displayTodos()
