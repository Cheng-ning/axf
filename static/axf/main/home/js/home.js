$(function () {
    init_newSwiper();
    init_Swiper1();

})

// 轮播
function init_newSwiper() {
    var newSwiper = new Swiper('#topSwiper',
                            {
                                loop:true,
                                autoplay:3000,
                                pagination:'.swiper-pagination',
                                autoplayDisableOnInteraction:false
                            })
}

function init_Swiper1() {
    var swiper1 = new Swiper('#swiperMenu',
        {
            slidesPerView:3,
        })

}