import React from 'react';
import { Link } from 'react-router-dom';

const DrugList = ({ drugs }) => {
    return (
        <ul className="drug-list">
            {drugs.map((drug) => (
                <li key={drug.rxcui} className="drug-item">
                    <Link to={`/drugs/${drug.name}`}>{drug.name}</Link>
                </li>
            ))}
        </ul>
    );
};

export default DrugList;
