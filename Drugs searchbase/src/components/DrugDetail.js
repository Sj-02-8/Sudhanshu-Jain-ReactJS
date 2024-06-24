import React, { useEffect, useState } from 'react';
import { getNDCs } from '../api';


const DrugDetail = ({ drug }) => {
    const [ndcs, setNdcs] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchNDCs = async () => {
            const result = await getNDCs(drug.rxcui);
            setNdcs(result.ndcGroup.ndcList.ndc || []);
            setLoading(false);
        };

        fetchNDCs();
    }, [drug.rxcui]);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div className="drug-detail">
            <h2>{drug.name}</h2>
            <p><strong>RXCUI:</strong> {drug.rxcui}</p>
            <p><strong>Synonyms:</strong> {drug.synonym}</p>
            <h3>NDCs:</h3>
            <ul>
                {ndcs.map(ndc => <li key={ndc}>{ndc}</li>)}
            </ul>
        </div>
    );
};

export default DrugDetail;
