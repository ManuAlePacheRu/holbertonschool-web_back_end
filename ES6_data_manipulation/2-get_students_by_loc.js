export default function getStudentsByLocation(studList, city) {
  const studLoc = studList.filter((student) => student.location === city);
  return studLoc;
}
