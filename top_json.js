fetch('companies.json')
    .then(response => response.json())
    .then(data => {
        const companies = data.companies;
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
                companyInfo.textContent = `${company.info}\nMore info: ${company.link}`;
                infoPanel.classList.add('active');
            });
            companyList.appendChild(companyIcon);
        });

        closePanelBtn.addEventListener('click', () => {
            infoPanel.classList.remove('active');
        });
    })
    .catch(error => console.error('Error loading company data:', error));
