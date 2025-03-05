import React, { useState } from "react";
import "./SpanQL.css";
import logo from "../images/logo.png";
import DataTableComponent from "./DataTableComponent";

const SpanQL = () => {
  const [consulta, setConsulta] = useState("");
  const [query, setQuery] = useState("");
  const [datosTabla, setDatosTabla] = useState(null);
  const [isLoading, setIsLoading] = useState(false); 

  const enviarConsulta = () => {
    setIsLoading(true); 
    const data = { consulta };

    fetch("https://spanql-backend.onrender.com", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        setQuery(data.resultado);
        if (data.datos_tabla !== "error") {
          setDatosTabla(data.datos_tabla);
        } else {
          setDatosTabla(null);
        }
      })
      .catch((error) => console.error("Error:", error))
      .finally(() => setIsLoading(false)); 
  };

  return (
    <div className="container">
      <header className="header">
        <img src={logo} alt="Icono de base de datos" className="icon" />
        <h1>SPANQL</h1>
        <img src={logo} alt="Icono de base de datos" className="icon" />
      </header>

      <div className="contenedor">
        <div className="content left">
          <label htmlFor="consulta">Consulta</label>
          <textarea
            id="consulta"
            rows="7"
            value={consulta}
            style={{ resize: "none" }}
            onChange={(e) => setConsulta(e.target.value)}
          ></textarea>

          <label htmlFor="query">Resultado</label>
          <textarea id="query" rows="7" value={query} style={{ resize: "none" }} disabled readOnly></textarea>

          <div>
            <button onClick={enviarConsulta}>Ejecutar</button>
          </div>
        </div>

        <div className="content right">
          {isLoading ? (
            <div className="spinner-container">
              <div className="spinner"></div>
              <p>Cargando datos...</p>
            </div>
          ) : datosTabla ? (
            <DataTableComponent datosTabla={datosTabla} />
          ) : (
            <>
              <h2>Tablas de prueba:</h2>
              <br />
              <ul>
                <li>departamentos</li><br />
                <li>empleados</li><br />
                <li>mascotas</li><br />
              </ul>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default SpanQL;
