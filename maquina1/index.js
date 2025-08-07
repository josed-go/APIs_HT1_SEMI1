const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;


app.use(cors());

app.get('/check', (req, res) => {
    res.status(200).send('OK');
});

app.get('/info', (req, res) => {
    res.status(200).json({ Instancia: 'Maquina 1 - API 1 (Javascript)', Curso: "Seminario de Sistemas 1 A", Grupo: "Grupo #9" });
});


const server = app.listen(port, () => {
    const host = server.address().address;
    const port = server.address().port;
    console.log(`Servidor escuchando en http://${host}:${port}`);
})