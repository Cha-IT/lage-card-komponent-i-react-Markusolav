import { Link } from 'react-router-dom';
import oppskrifter from './assets/oppskrifter.json';
import Header from './header.jsx';
import Nav from './nav.jsx';
import Card from './card.jsx';

function Oppskrifter() {
    return (
        <>
            <Header />
            <Nav />
            <h1>Oppskrifter</h1>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '16px', justifyContent: 'center' }}>
                {oppskrifter.map((oppskrift) => (
                    <Card
                        key={oppskrift.id}
                        title={oppskrift.navn}
                        description={oppskrift.beskrivelse}
                        image={oppskrift.bilde}
                        link={`/oppskrift/${oppskrift.id}`}
                    />
                ))}
            </div>
        </>
    );
}

export default Oppskrifter;