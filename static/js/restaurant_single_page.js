    document.addEventListener('click', function (e) {
        console.log('2defe')
        e.stopPropagation();
        // e.preventDefault();
        if (e.target.closest('.position-exit-cursor'))
        {
            document.querySelector('.table-restaurant-open-time').style.display = 'none'; 
        }
        else if (e.target.closest('.jquery-effect')) 
        {
            console.log('jquery')
            if(document.querySelector('.table-restaurant-open-time').style.display == 'none')
            {
                console.log('aa')
                document.querySelector('.table-restaurant-open-time').style.display = 'block';
            }
            else{
                console.log('bbb')
                document.querySelector('.table-restaurant-open-time').style.display = 'none';
            }
            
        }
        else if (e.target.closest('.table-restaurant-open-time')) 
        {
            console.log('Nothing to happened')
        }
        else 
        {
            document.querySelector('.table-restaurant-open-time').style.display = 'none';
        }
    })