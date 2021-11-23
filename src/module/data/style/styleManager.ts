import { spawn } from 'child_process'
import { DataDirectoryPath } from '../../../types/module/data/data.types'

export default class DataStyleManager {
  static getStylePath() {
    return `${DataDirectoryPath}/style`
  }

  static updateStyleData() {
    const result = spawn('./src/scripts/venv/Scripts/python', ['./src/scripts/scanConfig.py', ''])

    result.stdout.on('data', function (data) {
      if (data === undefined) return
      console.log(JSON.parse(data))
    })
  }

  static async run() {
    setInterval(() => {
      this.updateStyleData()
    }, 60 * 60 * 6 * 1000)
  }
}
