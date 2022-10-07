//ingredients add form
const addMoreBtn = document.getElementById('add-more')
const totalNewForms = document.getElementById('id_ingredient-TOTAL_FORMS')

addMoreBtn.addEventListener('click', add_new_form)
function add_new_form(event) {
    if (event) {
        event.preventDefault()
    }
    const currentIngredientForms = document.getElementsByClassName('edu_info-form')
    const currentFormCount = currentIngredientForms.length // + 1
    const formCopyTarget = document.getElementById('edu_info_list')
    const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', 'edu_info-form')
    copyEmptyFormEl.setAttribute('id', 'edu_info-${currentFormCount}')
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
    totalNewForms.setAttribute('value', currentFormCount + 1)
    // now add new empty form element to our html form
    formCopyTarget.append(copyEmptyFormEl)
}