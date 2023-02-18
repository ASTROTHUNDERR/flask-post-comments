
var textAreaVisible = false;

function toggleTextArea(postId) {
    var textArea = document.getElementById("myTextArea" + postId);
    var commentSubmit = document.getElementById('submit-button' + postId);
    if (textAreaVisible) {
      textArea.style.display = "none";
      textAreaVisible = false;
      commentSubmit.style.display = "none";
    } else {
      textArea.style.display = "block";
      textAreaVisible = true;
      commentSubmit.style.display = "block";
    }
  }
  


$(document).ready(function() {
    $("button").click(function() {
        var postId = $(this).data("id");
        var comment = $(this).siblings("textarea[name='post-comment']").val();
        $.ajax({
            url: "/posts",
            type: "POST",
            data: { "post_id": postId, "comment": comment },
            success: function(response) {
                alert(response);
            }
        });
    });
});
