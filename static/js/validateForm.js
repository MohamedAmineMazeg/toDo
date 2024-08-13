
const checkUserExist = () => 
{
const registrationForm = document.forms['registration-form']
const emailFormElement = registrationForm['email']
const usernameFormElement = registrationForm['username']
const emailAddress = emailFormElement.value
const username = usernameFormElement.value

axios.post('/validate-registration', {
    password: password,
})
.then( (response) => {
    
    if (response.data.userExist == 'true'){
        emailFormElement.setCustomValidity('This email address is already used, please choose another one')
    }
    if (response.data.emailExist == 'true'){
        emailFormElement.setCustomValidity('This username is already used, please choose another one')
    }

}, (error) = {

})
}  


const inputs = document.querySelectorAll('input');
const labels = document.querySelectorAll('label')
inputs.forEach((input) => {
    input.classList.remove('mb-2')
    input.classList.remove('mr-sm-2')
    input.classList.remove('mb-sm-0')
})

// labels.forEach((label) => {
//     label.classList.add('none');
// })