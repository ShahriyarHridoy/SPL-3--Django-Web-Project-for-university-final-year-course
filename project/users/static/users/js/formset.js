function updateElementIndex(el, prefix, ndx) {
  var id_regex = new RegExp("(" + prefix + "-\\d+)");
  var replacement = prefix + "-" + ndx;
  if ($(el).attr("for"))
    $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
  if (el.id) el.id = el.id.replace(id_regex, replacement);
  if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix, test, test2) {
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
  var conditionRow = $(selector.split(":")[0] + ":not(:last)");
  conditionRow
    .find(".btn." + test)
    .removeClass("btn-success")
    .addClass("btn-danger")
    .removeClass(test)
    .addClass(test2)
    .html("-");
  return false;
}
function deleteForm(prefix, btn, selector) {
  var total = parseInt($("#id_" + prefix + "-TOTAL_FORMS").val());
  if (total > 1) {
    btn.closest(selector).remove();
    var forms = $(selector);
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

//Education Information
$(document).on("click", ".add-form-row", function (e) {
  e.preventDefault();
  cloneMore(".form-row:last", "education", "add-form-row", "remove-form-row");
  return true;
});
$(document).on("click", ".remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("education", $(this), ".form-row");
  return false;
});

//Children Information
$(document).on("click", ".children-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".children-form-row:last",
    "children",
    "children-add-form-row",
    "children-remove-form-row"
  );
  return true;
});
$(document).on("click", ".children-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("children", $(this), ".children-form-row");
  return false;
});

//Traning Information
$(document).on("click", ".traning-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".traning-form-row:last",
    "traning",
    "traning-add-form-row",
    "traning-remove-form-row"
  );
  return true;
});
$(document).on("click", ".traning-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("traning", $(this), ".traning-form-row");
  return false;
});

//Posting Information
$(document).on("click", ".posting-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".posting-form-row:last",
    "posting",
    "posting-add-form-row",
    "posting-remove-form-row"
  );
  return true;
});
$(document).on("click", ".posting-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("posting", $(this), ".posting-form-row");
  return false;
});

//Promotion Information
$(document).on("click", ".promotion-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".promotion-form-row:last",
    "promotion",
    "promotion-add-form-row",
    "promotion-remove-form-row"
  );
  return true;
});
$(document).on("click", ".promotion-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("promotion", $(this), ".promotion-form-row");
  return false;
});

//Achievement Information
$(document).on("click", ".achievement-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".achievement-form-row:last",
    "achievement",
    "achievement-add-form-row",
    "achievement-remove-form-row"
  );
  return true;
});
$(document).on("click", ".achievement-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("achievement", $(this), ".achievement-form-row");
  return false;
});

//Leave Information
$(document).on("click", ".leave-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".leave-form-row:last",
    "leave",
    "leave-add-form-row",
    "leave-remove-form-row"
  );
  return true;
});
$(document).on("click", ".leave-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("leave", $(this), ".leave-form-row");
  return false;
});

//Other Service Information
$(document).on("click", ".otherService-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".otherService-form-row:last",
    "otherService",
    "otherService-add-form-row",
    "otherService-remove-form-row"
  );
  return true;
});
$(document).on("click", ".otherService-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("otherService", $(this), ".otherService-form-row");
  return false;
});

//Other Activities Information
$(document).on("click", ".otherActivities-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".otherActivities-form-row:last",
    "otherActivities",
    "otherActivities-add-form-row",
    "otherActivities-remove-form-row"
  );
  return true;
});
$(document).on("click", ".otherActivities-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("otherActivities", $(this), ".otherActivities-form-row");
  return false;
});

// R & D Project Information
$(document).on("click", ".r_and_d-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".r_and_d-form-row:last",
    "r_and_d",
    "r_and_d-add-form-row",
    "r_and_d-remove-form-row"
  );
  return true;
});
$(document).on("click", ".r_and_d-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("r_and_d", $(this), ".r_and_d-form-row");
  return false;
});

//Thesis Supervision Information
$(document).on("click", ".thesisSupervision-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".thesisSupervision-form-row:last",
    "thesisSupervision",
    "thesisSupervision-add-form-row",
    "thesisSupervision-remove-form-row"
  );
  return true;
});
$(document).on("click", ".thesisSupervision-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("thesisSupervision", $(this), ".thesisSupervision-form-row");
  return false;
});

//Research Interest Information
$(document).on("click", ".researchInterest-add-form-row", function (e) {
  e.preventDefault();
  cloneMore(
    ".researchInterest-form-row:last",
    "researchInterest",
    "researchInterest-add-form-row",
    "researchInterest-remove-form-row"
  );
  return true;
});
$(document).on("click", ".researchInterest-remove-form-row", function (e) {
  e.preventDefault();
  deleteForm("researchInterest", $(this), ".researchInterest-form-row");
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
