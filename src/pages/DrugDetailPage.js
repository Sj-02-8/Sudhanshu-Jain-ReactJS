import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getDrugs } from '../api';

import DrugDetail from '../components/DrugDetail';

const DrugDetailPage = () => {
    const { drug_name } = useParams();
    const [drug, setDrug] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchDrug = async () => {
            try {
                const result = await getDrugs(drug_name);
                if (result.drugGroup.conceptGroup) {
                    const foundDrug = result.drugGroup.conceptGroup.flatMap(group => group.conceptProperties || [])
                        .find(d => d.name.toLowerCase() === drug_name.toLowerCase());
                    setDrug(foundDrug || null);
                } else {
                    setError('Drug not found');
                }
            } catch (err) {
                setError('Error fetching data');
            }
            setLoading(false);
        };

        fetchDrug();
    }, [drug_name]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!drug) {
        return <div>Drug not found</div>;
    }

    return <DrugDetail drug={drug} />;
};

export default DrugDetailPage;
