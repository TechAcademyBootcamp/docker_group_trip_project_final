document.getElementById('search').addEventListener('input', function () {
    // console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
    var searchInput = document.getElementById('search');
    var inputValue = searchInput.value;
    // console.log(inputValue);
    $.ajax({
        url: 'http://localhost:8000/api/v1.0/cities/',
        method: 'GET',
        data: {
            'inputValue': inputValue,
        },
        success: function (response) {
            console.log(response);
            $('.empty').html('')
            let formDiv = $(`<div class="form-div w-100"><div>`);
           
            
            $('.empty').append(formDiv)
            if (inputValue) {
                for (let city of response) {
                    
                    
                    $('.form-div').append(`<a class="w-100" href=""><span class="ml-3">${city.name}</span></a>`)
                }
            }
        },
        error: function (error_response) {
            console.log(error_response);
        }
    })
});


// document.getElementById('search').addEventListener("click", function(){ 

//     $.ajax({
//         url: 'http://localhost:8000/api/v1.0/cities/',
//         method: 'GET',
//         data: {
//             'inputValue': inputValue,
//         },
//         success: function (response) {
//             console.log(response);
//             $('.empty').html('')
//             let formDiv = $(`<div class="form-div w-100"><div>`);
//             $('.empty').append(formDiv)
//             if (inputValue) {
//                 for (let city of response) {
//                     $('.form-div').append(`<a class="w-100" href="">${city.name}</a>`)
//                 }
//             }

//         },
//         error: function (error_response) {
//             console.log(error_response);
//         }
//     })
// });
