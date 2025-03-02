import React, { useState } from "react";
import DataTable from "react-data-table-component";
import "./DataTableComponent.css";

const paginationOptions = {
  rowsPerPageText: "Filas por página:",
  rangeSeparatorText: "de",
};

const DataTableComponent = ({ datosTabla }) => {
  // Verifica si los datos están definidos y no vacíos
  if (!datosTabla || Object.keys(datosTabla).length === 0) {
    return <p>No hay tablas disponibles</p>;
  }

  const tablas = Object.keys(datosTabla);
  const [indiceTabla, setIndiceTabla] = useState(0);

  const nombreTabla = tablas[indiceTabla];
  const { columns, data } = datosTabla[nombreTabla];

  // Verifica si las columnas están definidas
  if (!columns || !data) {
    return <p>No hay datos para mostrar.</p>;
  }

  const columnConfig = columns.map((col) => ({
    name: col.name.toUpperCase(),
    selector: (row) => row[col.name],
    sortable: true,
  }));

  return (
    <div className="tabla-container">
      <h3>{nombreTabla.toUpperCase()}</h3>
      <DataTable
        columns={columnConfig}
        data={data}
        pagination
        paginationComponentOptions={paginationOptions}
        paginationPerPage={5}
        paginationRowsPerPageOptions={[4, 6, 8, 10]}
        className="styled-table"
      />

      <div className="table-navigation">
        <button
          onClick={() =>
            setIndiceTabla((prev) => (prev > 0 ? prev - 1 : tablas.length - 1))
          }
        >
          ◀ Anterior
        </button>
        <button
          onClick={() =>
            setIndiceTabla((prev) => (prev < tablas.length - 1 ? prev + 1 : 0))
          }
        >
          Siguiente ▶
        </button>
      </div>
    </div>
  );
};

export default DataTableComponent;
