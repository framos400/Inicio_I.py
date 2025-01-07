function iniciarSimulacao() {
    const estados = [
        {
            nome: "São Paulo",
            populacao: 45000000,
            recursos: ["Água", "Minérios"],
        },
        {
            nome: "Fortaleza",
            populacao: 2687000,
            recursos: ["Turismo", "Petróleo"],
        }
    ];

    const municipios = [
        {
            nome: "São Paulo - Capital",
            populacao: 12300000,
            economia: "Indústria",
        },
        {
            nome: "Fortaleza - Capital",
            populacao: 2687000,
            economia: "Turismo",
        }
    ];

    // Atualizar a população dos estados (simulação de crescimento)
    estados.forEach(estado => {
        estado.populacao = Math.round(estado.populacao * 1.01); // Crescimento de 1%
    });

    // Mostrar os resultados na página
    const resultados = document.getElementById("resultados");
    resultados.innerHTML = "<h2>Resultados da Simulação</h2>";

    estados.forEach(estado => {
        resultados.innerHTML += `
            <p><strong>Estado:</strong> ${estado.nome}</p>
            <p><strong>População:</strong> ${estado.populacao}</p>
            <p><strong>Recursos:</strong> ${estado.recursos.join(", ")}</p>
            <hr>
        `;
    });

    municipios.forEach(municipio => {
        resultados.innerHTML += `
            <p><strong>Município:</strong> ${municipio.nome}</p>
            <p><strong>População:</strong> ${municipio.populacao}</p>
            <p><strong>Economia:</strong> ${municipio.economia}</p>
            <hr>
        `;
    });
}
