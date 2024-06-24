import React, { useState } from 'react';
import { getDrugs, getSpellingSuggestions } from '../api';
import SearchBar from '../components/SearchBar';
import DrugList from '../components/DrugList';

const SearchPage = () => {
    const [drugs, setDrugs] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSearch = async (query) => {
        setLoading(true);
        setError(null);
        try {
            const result = await getDrugs(query);
            if (result.drugGroup.conceptGroup) {
                const drugList = result.drugGroup.conceptGroup.flatMap(group => group.conceptProperties || []);
                setDrugs(drugList);
                if (drugList.length === 0) {
                    const suggestions = await getSpellingSuggestions(query);
                    if (suggestions.suggestionGroup.suggestionList.suggestion) {
                        setDrugs(suggestions.suggestionGroup.suggestionList.suggestion.map(s => ({ name: s })));
                    } else {
                        setError('No results found');
                    }
                }
            } else {
                setError('No results found');
            }
        } catch (err) {
            setError('Error fetching data');
        }
        setLoading(false);
    };

    return (
        <div>
            <SearchBar onSearch={handleSearch} />
            {loading ? <div>Loading...</div> : error ? <div>{error}</div> : <DrugList drugs={drugs} />}
        </div>
    );
};

export default SearchPage;
