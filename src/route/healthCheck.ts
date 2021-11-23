import express from 'express'

const router = express.Router()

router.get('/health-check', (_, res) => {
  res.json({ code: 200 })
})

export default router
