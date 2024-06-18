import React from 'react';
import logo from './logo.svg'; 
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SearchPage from './pages/SearchPage';
import DrugDetailPage from './pages/DrugDetailPage';
import './styles.css';
import './App.css';


function App() {
    return (
      <Router>
        <div className="App">
          <header className="App-header">
            <img src="/logo.png" alt="Logo" className="App-logo" />
          </header>
          <main>
            <Routes>
                <Route path="/drugs/search" element={<SearchPage />} />
                <Route path="/drugs/:drug_name" element={<DrugDetailPage />} />
                <Route path="/" element={<SearchPage />} />
            </Routes>
        </main>
      </div>
    </Router>
  );
}
export default App;
