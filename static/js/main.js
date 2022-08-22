$(document).ready(function(){
    $(document).on('submit', '#messageform', function(e){
        e.preventDefault

        $.ajax({
            type:'POST',
            url:'/send',

            data:{
                username:$('#username').val(),
                room:$('#room').val(),
                message:$('#message').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },

            success: function(data){
                alert(data)
            }
        });
        document.getElementById('message').value = ''
    });
})