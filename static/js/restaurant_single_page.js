$(document).ready(function () {

    document.querySelectorAll('.menu-list').forEach(function(menu){
        menu.addEventListener('click',function(){
        console.log('2')
        document.querySelectorAll('.all-menu-images').forEach(function(e){
            new PhotoViewer([{
                src: e.getAttribute('src'),
              },]);
        
            });
        })
    })
    //     new PhotoViewer([{
    //       src: 'https://farm1.staticflickr.com/313/31812080833_297acfbbd9_z.jpg',
    //     }, {
    //       src: 'https://farm4.staticflickr.com/3804/33589584740_b0fbdcd4aa_z.jpg',
    //     }, {
    //       src: 'https://farm1.staticflickr.com/470/31340603494_fb7228020d_z.jpg',
    //     }]);
  
    //   });

    $('.all-photos').click(function(){
        console.log('2')
        document.querySelector('.all-photos-page').classList.remove('d-none');
        document.querySelector('.all-photos-page').classList.add('d-block');
        document.querySelector('body').style.overflow='hidden'
      });
    $('.close-all-photos').click(function(){
        document.querySelector('.all-photos-page').classList.remove('d-block');
        document.querySelector('.all-photos-page').classList.add('d-none');
        document.querySelector('body').style.overflowY='scroll'
      });
    
    })

document.onclick = function (e){
        if (e.target.closest('.position-exit-cursor'))
        {
            document.querySelector('.table-restaurant-open-time').classList.remove("d-block"); 
            document.querySelector('.table-restaurant-open-time').classList.add("d-none"); 
        }
        else if (e.target.closest('.jquery-effect')) 
        {
            if(document.querySelector('.table-restaurant-open-time').classList.contains('d-none'))
            {
                document.querySelector('.table-restaurant-open-time').classList.remove("d-none"); 
                document.querySelector('.table-restaurant-open-time').classList.add("d-block"); 
            }
            else{
                document.querySelector('.table-restaurant-open-time').classList.remove("d-block"); 
                document.querySelector('.table-restaurant-open-time').classList.add("d-none"); 
            }
            
        }
        else if (!e.target.closest('.table-restaurant-open-time')) 
        {
            document.querySelector('.table-restaurant-open-time').classList.remove("d-block"); 
            document.querySelector('.table-restaurant-open-time').classList.add("d-none"); 
        }

    }

