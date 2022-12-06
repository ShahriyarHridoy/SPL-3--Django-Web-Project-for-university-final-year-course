// $(document).on("change", ".uploadProfileInput", function () {
//   var triggerInput = this;
//   var currentImg = $(this).closest(".pic-holder").find(".pic").attr("src");
//   var holder = $(this).closest(".pic-holder");
//   var wrapper = $(this).closest(".profile-pic-wrapper");
//   $(wrapper).find('[role="alert"]').remove();
//   triggerInput.blur();
//   var files = !!this.files ? this.files : [];
//   if (!files.length || !window.FileReader) {
//     return;
//   }
//   if (/^image/.test(files[0].type)) {
//     // only image file
//     var reader = new FileReader(); // instance of the FileReader
//     reader.readAsDataURL(files[0]); // read the local file

//     reader.onloadend = function () {
//       $(holder).addClass("uploadInProgress");
//       $(holder).find(".pic").attr("src", this.result);
//       $(holder).append(
//         '<div class="upload-loader"><div class="spinner-border text-primary" role="status"><span class="sr-only">Loading...</span></div></div>'
//       );

//       console.log("doing");
//       // Dummy timeout; call API or AJAX below
//       setTimeout(() => {
//         $(holder).removeClass("uploadInProgress");
//         $(holder).find(".upload-loader").remove();
//         // If upload successful
//         if (Math.random() < 0.9) {
//           $(wrapper).append(
//             '<div class="snackbar show" role="alert"><i class="fa fa-check-circle text-success"></i> Profile image updated successfully</div>'
//           );

//           // Clear input after upload
//           $(triggerInput).val("");

//           setTimeout(() => {
//             $(wrapper).find('[role="alert"]').remove();
//           }, 3000);
//         } else {
//           $(holder).find(".pic").attr("src", currentImg);
//           $(wrapper).append(
//             '<div class="snackbar show" role="alert"><i class="fa fa-times-circle text-danger"></i> There is an error while uploading! Please try again later.</div>'
//           );

//           // Clear input after upload
//           $(triggerInput).val("");
//           setTimeout(() => {
//             $(wrapper).find('[role="alert"]').remove();
//           }, 3000);
//         }
//       }, 1500);
//     };
//   } else {
//     $(wrapper).append(
//       '<div class="alert alert-danger d-inline-block p-2 small" role="alert">Please choose the valid image.</div>'
//     );
//     setTimeout(() => {
//       $(wrapper).find('role="alert"').remove();
//     }, 3000);
//   }
// });

$(document).ready(function () {
  $("#smartwizard").smartWizard({
    selected: 0,
    theme: "arrows",
    autoAdjustHeight: true,
    transitionEffect: "fade",
    showStepURLhash: true,
  });
});

//for date picker start
$(function () {
  $("#datepicker").datepicker();
});
$(function () {
  $("#datepicker1").datepicker();
});
$(function () {
  $("#datepicker2").datepicker();
});
$(function () {
  $("#datepicker3").datepicker();
});
$(function () {
  $("#datepicker4").datepicker();
});
$(function () {
  $("#datepicker5").datepicker();
});
$(function () {
  $("#datepicker6").datepicker();
});
$(function () {
  $("#datepicker7").datepicker();
});
//for date picker start

//for profile picure start

$(document).ready(function () {
  // Prepare the preview for profile picture
  // $("#pro_pic_url").readURL();
  $("#pro_pic").change(function () {
    readURL(this);
  });
});
function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $("#profile-PicturePreview").attr("src", e.target.result).fadeIn("slow");
    };
    reader.readAsDataURL(input.files[0]);
  }
}
//for profile picure end

//for signature picure start

$(document).ready(function () {
  // Prepare the preview for profile picture
  // $("#pro_pic_url").readURL();
  $("#signature_pic").change(function () {
    readURL1(this);
  });
});
function readURL1(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $("#signature-Preview").attr("src", e.target.result).fadeIn("slow");
    };
    reader.readAsDataURL(input.files[0]);
  }
}


//for signature picure end
