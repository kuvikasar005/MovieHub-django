var todaybtn = document.querySelector('#today-btn');
                    var tomorrowbtn = document.querySelector('#tomorrow-btn');
                    var nextdaybtn = document.querySelector('#nextday-btn');
                    
                    todaybtn.addEventListener('click', function(){
                            if(!todaybtn.classList.contains('active'))
                            {
                                    todaybtn.classList.add('active');
                            }
                            tomorrowbtn.classList.remove('active');
                            nextdaybtn.classList.remove('active');
                            document.querySelector('#today').style.display = 'block';
                            document.querySelector('#tomorrow').style.display = 'none';
                            document.querySelector('#nextday').style.display = 'none';
                    });
                    
                    tomorrowbtn.addEventListener('click', function(){
                            if(!tomorrowbtn.classList.contains('active'))
                            {
                                    tomorrowbtn.classList.add('active');
                            }
                            todaybtn.classList.remove('active');
                            nextdaybtn.classList.remove('active');
                            document.querySelector('#today').style.display = 'none';
                            document.querySelector('#tomorrow').style.display = 'block';
                            document.querySelector('#nextday').style.display = 'none';
                    });
                    
                    nextdaybtn.addEventListener('click', function(){
                            if(!nextdaybtn.classList.contains('active'))
                            {
                                    nextdaybtn.classList.add('active');
                            }
                            tomorrowbtn.classList.remove('active');
                            todaybtn.classList.remove('active');
                            document.querySelector('#today').style.display = 'none';
                            document.querySelector('#tomorrow').style.display = 'none';
                            document.querySelector('#nextday').style.display = 'block';
                    });

                    