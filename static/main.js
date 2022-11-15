axios.defaults.xsrfCookieName='csrftoken';
axios.defaults.xsrfHeaderName='X-CSRFTOKEN';

function create_item(){
    const title = document.getElementById('newToDoTitle').value
    const description = document.getElementById('newToDoDesc').value
    const due_date = document.getElementById('newToDoDueDate').value

    console.log(`CONSTANTS: ${title}, ${description}, ${due_date}`)
    
    axios.post('todos/new', {
        'title':title,
        'description': description,
        'due date': due_date,
    }).then((response)=>{console.log(response)})

}

function todo_page(){
    return
}

function display_list(){
    return
}

function edit_list(item){
    console.log(item)
    return 
}

function delete_task(item){
    console.log(item)
    return 
}