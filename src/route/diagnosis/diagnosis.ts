import express from 'express'
import { spawn } from 'child_process'

const router = express.Router()

router.post('/', async (req, res) => {
  const { imageId } = req.body

  if (imageId === undefined) {
    return res.json({ result: '올바르지 않은 요청입니다.' })
  }

  const result = spawn('./src/scripts/venv/Scripts/python', ['./src/scripts/color_extraction.py', imageId])

  result.stdout.on('data', function (data) {
    return res.json(JSON.parse(data))
  })

  result.stderr.on('data', function (data) {
    console.log(data.toString())
  })
})

export default router
