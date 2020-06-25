/*Calcul de fiabilité, disponibilité et MTBF */

/*Switch div_infos between them*/
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

/*add class active to the first link of machines */

const firstLink = document.querySelector('a[role = "tab"]');

if (firstLink != null) {
    firstLink.classList.add('active');

    /*add class show and active to the first div infos of machines */

    document.querySelector('div[role = "tabpanel"]').classList.add('show', 'active');   
}


