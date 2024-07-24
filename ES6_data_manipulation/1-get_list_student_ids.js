export default function getListStudentIds(studList) {
  if (!Array.isArray(studList) || students.length === 0) {
    return [];
  }
  const idsArray = studList.map((student) => student.id);
  return idsArray
}
