import React from 'react';
import Card from './Card';
import { shallow } from 'enzyme'

it('renders without crashing', () => {
    let card = {
        'english': 'test'
    }
    shallow(<Card card={card} />)
});
