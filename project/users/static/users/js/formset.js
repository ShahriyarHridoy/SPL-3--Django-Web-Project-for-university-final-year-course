//ingredients add form
// const addMoreBtn = document.getElementById('add-more')
// const totalNewForms = document.getElementById('id_ingredient-TOTAL_FORMS')

// addMoreBtn.addEventListener('click', add_new_form)
// function add_new_form(event) {
//     if (event) {
//         event.preventDefault()
//     }
//     const currentIngredientForms = document.getElementsByClassName('edu_info-form')
//     const currentFormCount = currentIngredientForms.length // + 1
//     const formCopyTarget = document.getElementById('edu_info_list')
//     const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
//     copyEmptyFormEl.setAttribute('class', 'edu_info-form')
//     copyEmptyFormEl.setAttribute('id', 'edu_info-${currentFormCount}')
//     const regex = new RegExp('__prefix__', 'g')
//     copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
//     totalNewForms.setAttribute('value', currentFormCount + 1)
//     // now add new empty form element to our html form
//     formCopyTarget.append(copyEmptyFormEl)
// }

function updateElementIndex(el, prefix, ndx) {
  var id_regex = new RegExp("(" + prefix + "-\\d+)");
  var replacement = prefix + "-" + ndx;
  if ($(el).attr("for"))
    $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
  if (el.id) el.id = el.id.replace(id_regex, replacement);
  if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
  var newElement = $(selector).clone(true);
  var total = $("#id_" + prefix + "-TOTAL_FORMS").val();
  newElement
    .find(
      ":input:not([type=button]):not([type=submit]):not([type=reset]):not([type=hidden])"
    )
    .each(function () {
      var name = $(this).attr("name");
      if (name) {
        name = name.replace("-" + (total - 1) + "-", "-" + total + "-");
        var id = "id_" + name;
        $(this).attr({ name: name, id: id }).val("").removeAttr("checked");
      }
    });
  newElement.find("label").each(function () {
    var forValue = $(this).attr("for");
    if (forValue) {
      forValue = forValue.replace("-" + (total - 1) + "-", "-" + total + "-");
      $(this).attr({ for: forValue });
    }
  });
  total++;
  $("#id_" + prefix + "-TOTAL_FORMS").attr("value", total);

  //   $().val(total);
  $(selector).after(newElement);
  var conditionRow = $(".form-row:not(:last)");
  conditionRow
    .find(".btn.add-form-row")
    .removeClass("btn-success")
    .addClass("btn-danger")
    .removeClass("add-form-row")
    .addClass("remove-form-row")
    .html("-");
  return false;
}
function deleteForm(prefix, btn) {
  var total = parseInt($("#id_" + prefix + "-TOTAL_FORMS").val());
  if (total > 1) {
    btn.closest(".form-row").remove();
    var forms = $(".form-row");
    $("#id_" + prefix + "-TOTAL_FORMS").val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
      $(forms.get(i))
        .find(":input")
        .each(function () {
          updateElementIndex(this, prefix, i);
        });
    }
  }
  return false;
}
$(document).on("click", ".add-form-row", function (e) {
  e.preventDefault();
  cloneMore(".form-row:last", "education");
  return true;
});
$(document).on("click", ".remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("education", $(this));
  return false;
});

// function updateElementIndex(el, prefix, ndx) {
//     var id_regex = new RegExp('(' + prefix + '-\\d+)');
//     var replacement = prefix + '-' + ndx;
//     if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
//     if (el.id) el.id = el.id.replace(id_regex, replacement);
//     if (el.name) el.name = el.name.replace(id_regex, replacement);
// }
// function cloneMore(selector, prefix) {
//     var newElement = $(selector).clone(true);
//     var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
//     newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
//         var name = $(this).attr('name')
//         if(name) {
//             name = name.replace('-' + (total-1) + '-', '-' + total + '-');
//             var id = 'id_' + name;
//             $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
//         }
//     });
//     newElement.find('label').each(function() {
//         var forValue = $(this).attr('for');
//         if (forValue) {
//           forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
//           $(this).attr({'for': forValue});
//         }
//     });
//     total++;
//     $('#id_' + prefix + '-TOTAL_FORMS').val(total);
//     $(selector).after(newElement);
//     var conditionRow = $('.form-row:not(:last)');
//     conditionRow.find('.btn.add-form-row')
//     .removeClass('btn-success').addClass('btn-danger')
//     .removeClass('add-form-row').addClass('remove-form-row')
//     .html('-');
//     return false;
// }
// function deleteForm(prefix, btn) {
//     var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
//     if (total > 1){
//         btn.closest('.form-row').remove();
//         var forms = $('.form-row');
//         $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
//         for (var i=0, formCount=forms.length; i<formCount; i++) {
//             $(forms.get(i)).find(':input').each(function() {
//                 updateElementIndex(this, prefix, i);
//             });
//         }
//     }
//     return false;
// }
// $(document).on('click', '.add-form-row', function(e){
//     e.preventDefault();
//     cloneMore('.form-row:last', 'form');
//     return false;
// });
// $(document).on('click', '.remove-form-row', function(e){
//     e.preventDefault();
//     deleteForm('form', $(this));
//     return false;
// });
