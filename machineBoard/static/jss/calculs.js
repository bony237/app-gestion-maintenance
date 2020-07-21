const calculDivAll = document.querySelectorAll(".calculDiv");

if (calculDivAll.length) {
  calculDivAll.forEach((calculDiv) => {
    const idToLookFor = calculDiv.dataset.machineId;
    const trDataAll = document.querySelectorAll(
      `tr[data-machine-id="${idToLookFor}"]`
    );
    console.log(trDataAll);
    let sumTA = 0,
      sumDurationIntervention = 0;

    trDataAll.forEach((trData) => {
      sumDurationIntervention += parseFloat(
        trData.dataset.durationIntervention
      );

      let TA = 0;
      let dateIntervention = trData.dataset.dateIntervention
        .split(".")
        .join("");
      let dateServiceOn = trData.dataset.dateServiceOn.split(".").join("");
      let dateDefaillance = trData.dataset.dateDefaillance.split(".").join("");

      if (trData.dataset.gravite == "3") {
        let date1 = new Date(dateServiceOn);
        let date2 = new Date(dateIntervention);

        TA = date1 - date2;

        TA += Math.floor(
          parseFloat(trData.dataset.durationIntervention) * 3600000
        );

        if (TA !== NaN) {
          sumTA += TA;
        }
      } else {
        let date1 = new Date(dateServiceOn);
        let date2 = new Date(dateDefaillance);
        TA = date1 - date2;

        TA += Math.floor(
          parseFloat(trData.dataset.durationIntervention) * 3600000
        );

        if (TA !== NaN) {
          sumTA += TA;
        }
      }
    });

    const MTBF = sumTA / trDataAll.length / 3600000;
    console.log(sumTA);
    const disponibility = sumDurationIntervention / trDataAll.length;

    calculDiv.querySelector(".mtbf").textContent = MTBF; // en heure
    calculDiv.querySelector(".disponibility").textContent = disponibility;
    calculDiv.querySelector(".fiability").textContent = 1 / MTBF;
  });
}
