import { spawn } from 'child_process'
import { DataDirectoryPath } from '../../../types/module/data/data.types'
import { existsSync, mkdirSync, writeFileSync, readFileSync } from 'fs'

export default class DataStyleManager {
  static getStylePath() {
    const defaultPath = `${DataDirectoryPath}/style`

    if (!existsSync(defaultPath)) {
      mkdirSync(defaultPath, { recursive: true })
    }

    return defaultPath
  }

  static getStyleList() {
    return JSON.parse(readFileSync(`${this.getStylePath()}/style.json`).toString())
  }

  static updateStyleData() {
    spawn('./src/scripts/venv/Scripts/python', ['./src/scripts/snap_musinsa.py'])
  }

  static async run() {
    // this.updateStyleData()
    // setInterval(() => {
    //   this.updateStyleData()
    // }, 60 * 60 * 6 * 1000)
  }

  static create() {}

  static delete() {}
}
