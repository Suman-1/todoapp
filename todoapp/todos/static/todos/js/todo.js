window.addEventListener('load', handleLoad);


function handleLoad() {
    var form = document.querySelector('.todo-form form');
    var message = document.querySelector('.alert-info');

    message.addEventListener('onload' , handleMessageBox);
    

    if (form) {
        var titleInput = document.querySelector('#input-todo-title');

        form.addEventListener('submit', handleFormSubmit);
        titleInput.addEventListener('keyup', handleTextCgange);
    }
}

function handleFormSubmit(e) {
    var titleInput = document.querySelector('#input-todo-title');
    var title = titleInput.value.trim();
    var oldColor = titleInput.style.borderColor;


    if (!title || title === '') {

        alert('Please enter the title.');
        titleInput.style.borderColor = 'red';
        titleInput.focus();
        e.preventDefault();
    }
    
   
}
function handleTextCgange() {
    console.log('text changed')
    var titleInput = document.querySelector('#input-todo-title');
    var oldColor = '#ccc';
        
    titleInput.style.borderColor = oldColor; 
}

function handleMessageBox() {
    var message = document.querySelector('.alert-info');

    console.log('text changed')
}

