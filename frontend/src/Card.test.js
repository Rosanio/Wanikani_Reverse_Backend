import React from 'react';
import Card from './Card';
import { shallow, mount } from 'enzyme'

it('renders without crashing', () => {
    let card = {
        'english': 'test'
    }
    shallow(<Card card={card} />)
});

it('recognizes correct answers', () => {
    let card = {
        'english': 'test',
        'kana': 'しけん',
        'kanji': '試験'
    }
    const component = mount(<Card card={card} />)
    component
        .find('#answer')
        .simulate('change', { target: { value: 'shikenn' } });
    component
        .find('#submit-answer')
        .simulate('submit');
    expect(component.state('correct')).toEqual(true);
    component.unmount()
})