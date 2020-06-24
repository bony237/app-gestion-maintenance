/*Calcul de fiabilité, disponibilité et MTBF */
const switchBtnAll = document.querySelectorAll('.switchBtn');


switchBtnAll.forEach((switchBtn) => {
    switchBtn.addEventListener('click', function() {
        const divToSwitch = this.parentElement.querySelectorAll('.infosToSwitch');
        console.log(divToSwitch.length);
        

        divToSwitch.forEach((div) => {
            div.classList.toggle('d-none');
            console.log(div);
        });
    });
});