
    $('.collapse').collapse()

    $('#myTab a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    })
    
    window.onscroll = function(){
        // console.log(window.pageYOffset)
        var element = document.querySelector('.mid-right');
        if(window.pageYOffset <= 2438 && window.pageYOffset >= 530){
            
            // console.log(element)
            this.document.querySelector('.route').style.position = 'fixed';
            this.document.querySelector('.route').style.top = '10px';
            this.document.querySelector('.route ul').style.position = '';
            // this.document.querySelector('.route ul').style.bottom = '10px';
            element.classList.add("offset-lg-3");
        }
        else if(window.pageYOffset > 2438){
            this.document.querySelector('.route').style.position = 'relative';
            this.document.querySelector('.route ul').style.position = 'absolute';
            this.document.querySelector('.route ul').style.bottom = '10px';
            
        }
        else{
            this.document.querySelector('.route').style.position = '';
            this.document.querySelector('.route').style.top = '';
            element.classList.remove("offset-lg-3");
        }
    }
    var expend_all = document.querySelector('.plus-img')
    var collapses = document.querySelectorAll('#accordion .collapse')
    expend_all.addEventListener("click", function(){
         console.log(collapses)

        });
    
