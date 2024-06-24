import axios from 'axios';

const BASE_URL = 'https://rxnav.nlm.nih.gov/REST';

export const getDrugs = async (name) => {
    const response = await axios.get(`${BASE_URL}/drugs.json?name=${name}`);
    return response.data;
};

export const getSpellingSuggestions = async (name) => {
    const response = await axios.get(`${BASE_URL}/spellingsuggestions.json?name=${name}`);
    return response.data;
};

export const getNDCs = async (rxcui) => {
    const response = await axios.get(`${BASE_URL}/rxcui/${rxcui}/ndcs.json`);
    return response.data;
};

 // Mock data for drug search
export const getmockDrugs = async (query) => {
   
    if (query.toLowerCase() === 'aspirin') {
      return { data: [{ name: 'Aspirin', rxcui: '12345' }] };
    }
    return { data: [] };
  };
  export const getmockSpellingSuggestions = async (query) => {
    // Mock data for spelling suggestions
    if (query.toLowerCase() === 'zyrte') {
      return { data: [{ suggestion: 'Zyrtec' }] };
    }
    return { data: [] };
  };
  export const getDrugDetails = async (drugName) => {
    // Mock data for drug details
    if (drugName.toLowerCase() === 'aspirin') {
      return { data: { rxcui: '12345', name: 'Aspirin', synonym: 'Acetylsalicylic Acid' } };
    }
    return { data: {} };
  };
  export const getmockNDCs = async (rxcui) => {
    // Mock data for NDCs
    if (rxcui === '12345') {
      return { data: [{ ndc: '12345-6789' }] };
    }
    return { data: [] };
  };
  