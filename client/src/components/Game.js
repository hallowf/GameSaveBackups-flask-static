import React from 'react'

export default function Game({ game }) {
  return <pre>Game: {JSON.stringify(game, null, 2)}</pre>
}
