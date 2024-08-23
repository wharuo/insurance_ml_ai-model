const companies = [
    { name: "Manulife", icon: "icons/manulife.png", info: "Translated info from Mordor Intelligence." },
    { name: "Great-West Lifeco", icon: "icons/great-west.png", info: "Translated info from Mordor Intelligence." },
    { name: "Sun Life Financial", icon: "icons/sun-life.png", info: "Translated info from Mordor Intelligence." },
    { name: "Fairfax Financial", icon: "icons/fairfax.png", info: "Translated info from Mordor Intelligence." },
    { name: "Intact Financial", icon: "icons/intact.png", info: "Translated info from Mordor Intelligence." },
    { name: "Industrial Alliance", icon: "icons/industrial-alliance.png", info: "Translated info from Mordor Intelligence." },
    { name: "Power Corporation", icon: "icons/power-corp.png", info: "Translated info from Mordor Intelligence." },
    { name: "RBC Insurance", icon: "icons/rbc.png", info: "Translated info from Mordor Intelligence." },
    { name: "TD Insurance", icon: "icons/td.png", info: "Translated info from Mordor Intelligence." },
    { name: "Desjardins", icon: "icons/desjardins.png", info: "Translated info from Mordor Intelligence." },
];

const companyList = document.querySelector('.company-list');
const infoPanel = document.getElementById('info-panel');
const companyName = document.getElementById('company-name');
const companyInfo = document.getElementById('company-info');
const closePanelBtn = document.getElementById('close-panel');

companies.forEach(company => {
    const companyIcon = document.createElement('img');
    companyIcon.src = company.icon;
    companyIcon.alt = company.name;
    companyIcon.classList.add('company-icon');
    companyIcon.addEventListener('click', () => {
        companyName.textContent = company.name;
        companyInfo.textContent = company.info;
        infoPanel.classList.add('active');
    });
    companyList.appendChild(companyIcon);
});

closePanelBtn.addEventListener('click', () => {
    infoPanel.classList.remove('active');
});
