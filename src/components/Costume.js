import React from 'react'
import { Card, Button } from 'react-bootstrap'

const Costume = ({costume}) => {
  return (
    <Card style={{ width: '18rem' }}>
      <Button variant="primary"><i className="fas fa-bookmark"></i></Button>
      <Card.Img variant="top" src={costume.image} />
      <Card.Body>
        <Card.Title>{costume.title}</Card.Title>
        <Button variant="primary">
            <img src={'../assets/star.png'}></img>
        </Button>
      </Card.Body>
    </Card>
  )
}

export default Costume