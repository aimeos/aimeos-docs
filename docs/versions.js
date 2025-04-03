(function() {

	let nodes = document.getElementsByClassName("version-select");

	for(let i=0; i < nodes.length; i++) {

		if(nodes[i].tagName === 'SELECT') {

			['latest', '2025.x', '2024.x', '2023.x', '2022.x', '2021.x', '2020.x'].forEach(function(el) {
				let option = document.createElement("option");
				option.appendChild(document.createTextNode(el));
				nodes[i].appendChild(option);
			});

			nodes[i].value = window.location.pathname.slice(6, 12);

			nodes[i].addEventListener('change', function() {
				window.location = "//" + window.location.hostname + ":" + window.location.port + "/docs/" + nodes[i].value;
			});
		}
	}

})();
