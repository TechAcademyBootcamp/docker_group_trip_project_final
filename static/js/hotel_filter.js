document.querySelector('#search-button-1').addEventListener('click',(e)=>{
    e.preventDefault();
    var cityName=document.querySelector('#city-name').value
    var selectedBed = document.getElementById("selected-beds").value;
    var selectedChildCount = document.getElementById("selected-child-count").value;
    var selectedRoomCount = document.getElementById("selected-room-count").value;
    var all_data = {
        'cityName':cityName,
        'selectedBed' : selectedBed,
        'selectedChildCount':selectedChildCount,
        'selectedRoomCount':selectedRoomCount,
    }
    var api_url = document.querySelector('#url').dataset.url;
    const new_url = 'asdasdasda'
    $.ajax({
        url: new_url,
        method: "POST",
        data: all_data,

        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    })
})