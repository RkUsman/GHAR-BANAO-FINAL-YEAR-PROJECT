
$('.remove-cart').click(function(){
    var id = $(this).attr("pid").tostring();
    var eml = this
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success: function(data){
            console.log("Delete")
            document.getElementById("amount").innerText=data.amount
            document.getElementById("total_amount").innerText=data.total_amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }

    })
})