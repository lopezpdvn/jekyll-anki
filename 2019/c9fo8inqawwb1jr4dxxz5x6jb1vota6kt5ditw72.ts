import { StrVal } from './module_1';

export const numberRegexp = /^[0-9]+$/;

export class ZipCodeValidator implements StrVal {
  isAcceptable(s: string) {
    return s.length === 5 &&
           numberRegexp.test(s);
  }
}